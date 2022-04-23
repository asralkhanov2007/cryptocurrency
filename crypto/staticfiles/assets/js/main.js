// Объект с курсами криптоВалют
const rates = {
    "BITCOIN":180,
    "NEO":120,
    "DASH":100,

}

// Элементы формы, ввод суммы, выбор валюты, поле с резльтатом
const input = document.querySelector('#input');
const result = document.querySelector('#result');
const select = document.querySelector('#select');


input.oninput = function(){
    console.log('Changed');
    result.value = (parseFloat(input.value) / rates[select.value].Value).toFixed(2);
    
}

select.oninput = function(){
    console.log('Changed');
    result.value = (parseFloat(input.value) / rates[select.value].Value).toFixed(2);

}

// input.oninput = convertValue;

// select.oninput = convertValue;

// // Функция конвертации
// function convertValue() {

//     result.value = (parseFloat(input.value) / rates[select.value].Value).toFixed(2);

// }

