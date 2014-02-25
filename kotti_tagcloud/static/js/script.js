// For more informations and a list of the possible options have
// a look to http://www.goat1000.com/tagcanvas.php.
$(function() {
    $(document).ready(function() {
        function start_canvas() {
            if(!jQuery('#tags-canvas').tagcanvas({
                textColour : '#000000',
                outlineColour: '#cccccc',
                outlineThickness: 3,
                outlineOffset: 3,
                maxSpeed : 0.05,
                freezeActive : false,
                decel: 0.99,
                initial: [0.8, -0.3],
                noMouse: false,
                wheelZoom: false,
                imageScale: null,
                depth : 0.9
            }, 'tags')) {
                // TagCanvas failed to load
                $('#canvas-container').hide();
            }
        }
        start_canvas();
    });
});
