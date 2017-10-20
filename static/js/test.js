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
                          timeout: 200000000,
                          data: {
                            operation: "searchSong",
                            term: request.term
                          },
                          success: function( data ) {
                            response(data.results);
                          }
                        } );
                      },
                      minLength: 2,
                      select: function( event, ui ) {
                        console.log( "Selected: " + ui.item.value + " aka " + ui.item.id );
                      }
            });

}
