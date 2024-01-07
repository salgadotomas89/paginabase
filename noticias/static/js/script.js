(function () {
    'use strict';

    var form = document.getElementById('noticia-form');

    form.addEventListener('submit', function (event) {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }

      form.classList.add('was-validated');
    }, false);
  })();

  document.addEventListener('DOMContentLoaded', function () {
    const deleteLinks = document.querySelectorAll('.delete-link');

    function deleteNoticia(id) {
      $.ajax({
        type: 'DELETE',
        url: `/noticias/delete/${id}`,
        headers: {
          'X-CSRFToken': '{{ csrf_token }}',
        },
        success: function (data) {
          const deletedNoticia = document.querySelector(`[data-id="${id}"]`);
          if (deletedNoticia) {
            deletedNoticia.closest('.col-md-6').remove();
          }

        },
        error: function (error) {
          console.error('Error al eliminar noticia:', error);
        }
      });
    }

    deleteLinks.forEach(link => {
      link.addEventListener('click', function (event) {
        event.preventDefault();
        const id = this.getAttribute('data-id');
        if (confirm('¿Estás seguro de que quieres eliminar esta noticia?')) {
          deleteNoticia(id);
        }
      });
    });
  });