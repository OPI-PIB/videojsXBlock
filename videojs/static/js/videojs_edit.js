/* Javascript for videojsXBlock. */
function videojsXBlockInitStudio(runtime, element) {
    var language_list = $(".subtitle_text",element)
    language_list.sort((a,b) => { 
        
        if ($(a).data("code") === 'en') return -1;
        if ($(b).data("code") === 'en') return 1;
        
        return $(a).data("language").localeCompare($(b).data("language"))
    });
    
    language_list.each(function() {
      if(!$(this).val().trim().length && $(this).attr("data-code") !== 'pl')
      {
          $("#select_add_language").append(new Option($(this).attr("data-language"), $(this).attr("data-code")));
          $(this).parents(".field").hide();
      }
    });

    $("#add_lang_btn").click(function (){
        var code = $("#select_add_language").val();
        $("#lang-"+code).show();
        location.hash = "#lang-" + code;
        $("#select_add_language option:selected").remove();
    });

    $(".remove_lang_btn").click(function (){
        var textarea = $(this).parent().next('textarea');
        $(textarea).val("");
        $("#select_add_language").append(new Option($(textarea).attr("data-language"), $(textarea).attr("data-code")));
        $(textarea).parents(".comp-setting-entry").hide();
    });





    $(element).find('.action-cancel').bind('click', function () {
        runtime.notify('cancel', {});
    });

    $(element).find('.action-save').bind('click', function () {
        var data = {
            'display_name': $('#videojs_edit_display_name').val(),
            'url': $('#videojs_edit_url').val(),
        };

        $(".subtitle_text").each(function (index) {
            data['subtitle_text_' + $(this).attr("data-code")] = $(this).val();
        });

        runtime.notify('save', {state: 'start'});

        var handlerUrl = runtime.handlerUrl(element, 'save_videojs');
        $.post(handlerUrl, JSON.stringify(data)).done(function (response) {
            if (response.result === 'success') {
                runtime.notify('save', {state: 'end'});
                // Reload the whole page :
                // window.location.reload(false);
            } else {
                runtime.notify('error', {msg: response.message})
            }
        });
    });
}
