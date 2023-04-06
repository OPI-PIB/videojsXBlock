/* Javascript for videojsXBlock. */
function videojsXBlockInitView(runtime, element) {
    /* Weird behaviour :
     * In the LMS, element is the DOM container.
     * In the CMS, element is the jQuery object associated*
     * So here I make sure element is the jQuery object */
    if (element.innerHTML) element = $(element);

    var video = element.find('video:first');
    var player = videojs(video.get(0), {
        language: 'pl',
        textTrackSettings: true,
        playbackRates: [0.5, 1, 1.5, 2]
    }, function() {
        var player = this;
     
        player.controlBar.addChild('QualitySelector');
     });

    
}
