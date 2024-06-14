


document.addEventListener('DOMContentLoaded', function () {
  const myModal = document.getElementById('myModal')
  myModal.addEventListener('shown.bs.modal', () => {

    var button = event.relatedTarget; // Elemento que acionou o modal
    var rifaId = button.getAttribute('data-rifa-id');
    var numeroId = button.getAttribute('data-numero-id');

    // Use rifaId e numeroId conforme necessário
    console.log('Rifa ID:', rifaId);
    console.log('Número ID:', numeroId);

    // Adicionando a ação ao botão de "Save changes"
    var saveButton = document.getElementById('saveChangesButton');
    saveButton.onclick = function () {
        window.location.href = `/rifa/edit_rifa/${rifaId}/${numeroId}`;
    };
  })
});
  