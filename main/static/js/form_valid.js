document.addEventListener('DOMContentLoaded', function() {
    // Валидация телефона
    const phoneInput = document.getElementById('phone');
    
    if (phoneInput) {
        // Установка значения по умолчанию при фокусе
        phoneInput.addEventListener('focus', function() {
            if (!this.value) {
                this.value = '+7';
            }
        });
        
        // Применение маски при вводе
        phoneInput.addEventListener('input', function(e) {
            // Удаляем все нецифровые символы, кроме "+"
            let value = this.value.replace(/[^\d+]/g, '');
            
            // Проверяем, начинается ли с "+7", если нет - исправляем
            if (!value.startsWith('+7')) {
                if (value.startsWith('+')) {
                    value = '+7' + value.substring(1);
                } else {
                    value = '+7' + value;
                }
            }
            
            // Форматируем номер по маске +7-XXX-XXX-XX-XX
            let formattedValue = '+7';
            if (value.length > 2) {
                // Добавляем первый блок из 3 цифр
                const firstBlock = value.substring(2, Math.min(5, value.length));
                if (firstBlock) {
                    formattedValue += '-' + firstBlock;
                }
                
                // Добавляем второй блок из 3 цифр
                if (value.length > 5) {
                    const secondBlock = value.substring(5, Math.min(8, value.length));
                    formattedValue += '-' + secondBlock;
                    
                    // Добавляем третий блок из 2 цифр
                    if (value.length > 8) {
                        const thirdBlock = value.substring(8, Math.min(10, value.length));
                        formattedValue += '-' + thirdBlock;
                        
                        // Добавляем четвертый блок из 2 цифр
                        if (value.length > 10) {
                            const fourthBlock = value.substring(10, Math.min(12, value.length));
                            formattedValue += '-' + fourthBlock;
                        }
                    }
                }
            }
            
            // Устанавливаем отформатированное значение
            this.value = formattedValue;
        });
    }
    
    // Валидация имени
    const nameInput = document.getElementById('id_name');
    
    if (nameInput) {
        // Добавляем визуальную обратную связь при вводе
        nameInput.addEventListener('input', function() {
            if (this.value.trim() === '') {
                this.classList.add('error');
                // Можно добавить сообщение об ошибке рядом с полем
                let errorMsg = this.nextElementSibling;
                if (!errorMsg || !errorMsg.classList.contains('name-error')) {
                    errorMsg = document.createElement('span');
                    errorMsg.classList.add('name-error');
                    errorMsg.textContent = 'Имя не должно быть пустым';
                    this.parentNode.insertBefore(errorMsg, this.nextSibling);
                }
            } else {
                this.classList.remove('error');
                // Удаляем сообщение об ошибке, если оно есть
                const errorMsg = this.nextElementSibling;
                if (errorMsg && errorMsg.classList.contains('name-error')) {
                    errorMsg.remove();
                }
            }
        });
    }
    
    // Проверка формы перед отправкой
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function(event) {
            let hasErrors = false;
            
            // Проверка телефона
            if (phoneInput) {
                const phoneValue = phoneInput.value;
                const phonePattern = /^\+7-\d{3}-\d{3}-\d{2}-\d{2}$/;
                
                if (!phonePattern.test(phoneValue)) {
                    event.preventDefault();
                    alert('Пожалуйста, введите номер телефона в формате +7-XXX-XXX-XX-XX');
                    phoneInput.focus();
                    hasErrors = true;
                }
            }
            
            // Проверка имени
            if (nameInput && nameInput.value.trim() === '') {
                event.preventDefault();
                if (!hasErrors) { // Показываем только одно сообщение за раз
                    alert('Пожалуйста, введите ваше имя');
                    nameInput.focus();
                }
                nameInput.classList.add('error');
                hasErrors = true;
            }
        });
    }
});