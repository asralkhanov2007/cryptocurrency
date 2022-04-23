
window.onload = function () {
    let c = {'BITCOIN':'200', 'DASH':'150', 'NEO':'4'}; // Устанавливаем курс валют

    let val = document.getElementById('input'); // Получаем элемент ввода данных
    let select = document.getElementById('select'); // Получаем первый селект
    let select2 = document.getElementById('select2'); // Получаем второй селект
    let result = document.getElementsByClassName('result')[0]; // Получаем поле куда будем писать результат
    function summ() { // Делаем функцию
        let z = 0;
        if(select.value === select2.value){ // Если оба значения в селектах равны
            result.innerText = val.value; // То просто вписываем данные из поля ввода
        } else {
            if(select.value != 'BITCOIN'){ // Если не равны рублю, то
                z = val.value*c[select.value]; // Переводим сумму в рубли
                result.innerHTML = Math.ceil((z/c[select2.value])*100)/100; // Делим на курс и округляем до сотых
            } else { // Если не равны
                result.innerHTML = Math.ceil((val.value*c[select2.value])*100)/100; // Умножаем на курс и округляем до сотых
            }
        }
    }
    val.oninput = function () { // При вводе данных в поле вызываем функцию.
        summ();
    };
    select.onchange = function () { // При смене первого селекта вызываем функцию.
        summ();
    };
    select2.onchange = function () { // При смене второго селекта вызываем функцию.
        summ();
    }
}

function myFunction() {
    /* Получить текстовое поле */
    var copyText = document.getElementById("myInput");
  
    /* Выделите текстовое поле */
    copyText.select();
    copyText.setSelectionRange(0, 99999); /* Для мобильных устройств */
  
    /* Скопируйте текст внутри текстового поля */
    document.execCommand("copy");
  
    /* Оповещение скопированного текста */
    alert("Скопировал текст: " + copyText.value);
  }