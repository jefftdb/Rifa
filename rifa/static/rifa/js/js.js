


document.addEventListener('DOMContentLoaded', function () {
  const myModal = document.getElementById('myModal');
  myModal.addEventListener('show.bs.modal', function (event) {
      var button = event.relatedTarget; // Elemento que acionou o modal
      var rifaId = button.getAttribute('data-rifa-id');
      var numeroId = button.getAttribute('data-numero-id');
      
      // Use rifaId e numeroId conforme necessário
      console.log('Rifa ID:', rifaId);
      console.log('Número ID:', numeroId);

      // Atualize a URL para a requisição AJAX
      var url = `/pagamento/pix/${rifaId}/${numeroId}`;

    // Exibir o spinner de carregamento e ocultar o conteúdo do modal
    document.getElementById('loadingSpinner').style.display = 'block';
    document.getElementById('modalContent').style.display = 'none';

      // Faça a requisição AJAX
      $.ajax({
          url: url,
          type: "GET",
          dataType: "json",
          success: (data) => {
              console.log(data);

              // Atualize o conteúdo do modal com os dados recebidos
              
              document.getElementById('modalQRCode').src = data.QR_img || '';
              document.getElementById('modalTextoPix').value = data.texto_pix || 'N/A';

              //document.getElementById('modalRifaTitle').innerText = data.rifa || 'N/A';
              //document.getElementById('modalOrderId').innerText = data.order_id || 'N/A';
              //document.getElementById('modalCustomerName').innerText = data.customer_name || 'N/A';
              //document.getElementById('modalCustomerEmail').innerText = data.customer_email || 'N/A';
              //document.getElementById('modalCustomerTaxId').innerText = data.customer_tax_id || 'N/A';
              //document.getElementById('modalCustomerPhone').innerText = data.customer_phone || 'N/A';
              //document.getElementById('modalItemName').innerText = data.item_name || 'N/A';
              //document.getElementById('modalItemQuantity').innerText = data.item_quantity || 'N/A';
              //document.getElementById('modalItemAmount').innerText = data.item_amount || 'N/A';
              // Ocultar o spinner de carregamento e exibir o conteúdo do modal
              document.getElementById('loadingSpinner').style.display = 'none';
              document.getElementById('modalContent').style.display = 'block';
      },
      error: (error) => {
          console.log(error);

          // Ocultar o spinner de carregamento mesmo em caso de erro
          document.getElementById('loadingSpinner').style.display = 'none';
          document.getElementById('modalContent').style.display = 'block';
      }
  });

      // Adicionando a ação ao botão de "Save changes"
      var saveButton = document.getElementById('saveChangesButton');
      saveButton.onclick = function () {
          window.location.href = `/rifa/edit_rifa/${rifaId}/${numeroId}`;
      };
  });
    // Função para copiar o código Pix para a área de transferência
    document.getElementById('copyButton').addEventListener('click', function() {
        var pixCodeInput = document.getElementById('modalTextoPix');
        
        // Seleciona o conteúdo do input
        pixCodeInput.select();
        pixCodeInput.setSelectionRange(0, 99999); // Para dispositivos móveis

        // Copia o conteúdo selecionado para a área de transferência
        document.execCommand('copy');
        
        // Mostrar mensagem de alerta
        var copyAlert = document.getElementById('copyAlert');
        copyAlert.style.display = 'block';
        setTimeout(function() {
            copyAlert.style.display = 'none';
        }, 2000);
    });
});

