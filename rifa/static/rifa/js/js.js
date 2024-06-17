


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

      // Faça a requisição AJAX
      $.ajax({
          url: url,
          type: "GET",
          dataType: "json",
          success: (data) => {
              console.log(data);

              // Atualize o conteúdo do modal com os dados recebidos
              document.getElementById('modalRifaTitle').innerText = data.rifa || 'N/A';
              document.getElementById('modalQRCode').src = data.QR_img || '';
              document.getElementById('modalTextoPix').innerText = data.texto_pix || 'N/A';
              document.getElementById('modalOrderId').innerText = data.order_id || 'N/A';
              document.getElementById('modalCustomerName').innerText = data.customer_name || 'N/A';
              document.getElementById('modalCustomerEmail').innerText = data.customer_email || 'N/A';
              document.getElementById('modalCustomerTaxId').innerText = data.customer_tax_id || 'N/A';
              document.getElementById('modalCustomerPhone').innerText = data.customer_phone || 'N/A';
              document.getElementById('modalItemName').innerText = data.item_name || 'N/A';
              document.getElementById('modalItemQuantity').innerText = data.item_quantity || 'N/A';
              document.getElementById('modalItemAmount').innerText = data.item_amount || 'N/A';
          },
          error: (error) => {
              console.log(error);
          }
      });

      // Adicionando a ação ao botão de "Save changes"
      var saveButton = document.getElementById('saveChangesButton');
      saveButton.onclick = function () {
          window.location.href = `/rifa/edit_rifa/${rifaId}/${numeroId}`;
      };
  });
});
  