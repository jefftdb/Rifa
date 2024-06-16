(function(win, doc){
    if(doc.querySelector('#FormCard')){
        let formCard = doc.querySelector('#FormCard');
        formCard.addEventListener('submit', (e) => {
            e.preventDefault();

            let csrfToken = doc.querySelector('input[name="csrfmiddlewaretoken"]').value;

            let card = PagSeguro.encryptCard({
                publicKey: csrfToken,
                holder: doc.querySelector('#cardHolder').value,
                number: doc.querySelector('#cardNumber').value,
                expMonth: doc.querySelector('#cardMonth').value,
                expYear: doc.querySelector('#cardYear').value,
                securityCode: doc.querySelector('#cardCVV').value,
            });
            
            let encrypted = card.encryptedCard;
            doc.querySelector('#encryptedCard').value = encrypted;                        
           
            formCard.submit();
        });
    }
})(window, document);