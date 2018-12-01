var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
    '/static/core/css/Estilos.css',
    '/static/core/css/bootstrap.min.css',
    '/static/core/img/Apolo.jpg',
    '/static/core/img/Bigotes.jpg', 
    '/static/core/img/Chocolate.jpg', 
    '/static/core/img/crowfunding.jpg', 
    '/static/core/img/deleteUser.png', 
    '/static/core/img/Duque.jpg', 
    '/static/core/img/logo.png', 
    '/static/core/img/Luna.jpg',
    '/static/core/img/Maya.jpg', 
    '/static/core/img/modificarUser.png', 
    '/static/core/img/Oso.jpg', 
    '/static/core/img/perro.png', 
    '/static/core/img/Pexel.jpg', 
    '/static/core/img/rescate.jpg', 
    '/static/core/img/socialfacebook.png',
    '/static/core/img/social-inst.png', 
    '/static/core/img/socialplus.png', 
    '/static/core/img/social-twitter.png', 
    '/static/core/img/Tom.jpg', 
    '/static/core/img/Wifi.jpg', 
    '/static/core/js/inicializacion.js',
    '/static/core/js/combo.js',
    '/static/core/js/formato_rut.js',
    '/static/core/js/isEmail.js',
    '/static/core/js/jquery.validate.min.js',
    '/static/core/js/soloLetras.js',
    '/static/core/js/Valida_Rut.js',
    '/static/core/js/valida.js',
    '/static/core/js/validacion.js',
    '/static/core/js/validaNumericos.js',
    '/static/core/js/validarRUT.js',
    '/static/core/js/bootstrap.min.js',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://cdnjs.cloudflare.com/ajax/libs/fancybox/3.4.1/jquery.fancybox.min.css'



];

self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
            if(response) {
                return response;
            }

            return fetch(event.request);
        })
    );
});