(() => {
    // Definición del tipo de elemento HTML
    type HtmlType = 'input' | 'select' | 'textarea' | 'radio';

    // Clase base para elementos HTML
    class HtmlElement {
        constructor(
            public id: string,
            public type: HtmlType,
        ) {}
    }

    // Clase para atributos de un input
    class InputAttributes {
        constructor(
            public value: string,
            public placeholder: string,
        ) {}
    }

    // Clase para eventos de un input
    class InputEvents {
        constructor(
            private htmlElement: HtmlElement,
            private attributes: InputAttributes,
        ) {}

        // Establece el foco en el input
        setFocus() {
            console.log(`Foco en el elemento con id: ${this.htmlElement.id}`);
        }

        // Obtiene el valor del input
        getValue() {
            return this.attributes.value;
        }

        // Verifica si el input está activo
        isActive() {
            return document.activeElement?.id === this.htmlElement.id;
        }

        // Elimina el valor del input
        removeValue() {
            this.attributes.value = '';
        }
    }

    // Creación de un nuevo campo de nombre
    const nameField = new InputEvents(
        new HtmlElement('txtName', 'input'),
        new InputAttributes('Fernando', 'Enter first name')
    );

    console.log({ nameField });

})();
