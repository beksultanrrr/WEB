let id = Symbol("id");
alert(id.toString()); // Symbol(id), now it works


let id = Symbol("id");
alert(id.description); // id Или получите свойство symbol.description, чтобы показать только описание: