window.onload = function(){


//        $('#search-next-song-input').on('keyup',function(){
//            alert($(this).val());
//        });


            $( "#search-next-song-input" ).autocomplete({
              //source: availableTags
              source: function( request, response ) {
                        $.ajax( {
                          method: "post",
                          url: "searchSongService",
                          data: {
                            operation: "searchSong",
                            term: request.term
                          },
                          success: function( data ) {
                            console.log(data );
                            response(data);
                          }
                        } );
                      },
                      minLength: 2,
                      select: function( event, ui ) {
                        log( "Selected: " + ui.item.value + " aka " + ui.item.id );
                      }
            });

}
