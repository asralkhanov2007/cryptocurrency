// Объект с курсами криптоВалют
const rates = {}

// Элементы для отображения курса криптоВалют
const elementUSD = 100 ;
const elementEUR = 150 ;
const elementGBP = 200 ;

// Элементы формы, ввод суммы, выбор валюты, поле с резльтатом
const input = document.querySelector('#input');
const result = document.querySelector('#result');
const select = document.querySelector('#select');

getCurrecies()

async function getCurrecies() {

    rates.USD = 100
    rates.EUR = 200
    rates.GBP = 50
    
    console.log(rates);
}

input.oninput = function() {
    console.log('Changed!');
    result.value = (parseFloat(nput.value) / rates[select.value].Value).toFixed(2);
}

// input.oninput = convertValue;

// select.oninput = convertValue;

// // Функция конвертации
// function convertValue() {

//     result.value = (parseFloat(input.value) / rates[select.value].Value).toFixed(2);

// }
