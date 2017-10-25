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
                        var addingSongToMyMusic = addSongToMyMusic(ui.item.id);
                        addingSongToMyMusic.done(function(){
                            alert('Agregada correctamente');
                        })
                      }
            });
            if($('#hola').length){
                $('#hola').on('click',function(){
                    $('#current-offset').val(0);
                    getAndPutSongs(0);
                });
            }

            function getAndPutSongs(offset){
                var gettingTracks = getUserTracks(offset);
                    gettingTracks.done(function(data){
                        var tracks = data;
                        console.log(tracks);
                        var html = '<ul>';
                        tracks.forEach(function(o){
                            html = html + '<li id="'+o.track.id+'"><input name="tracks-elegibles" data-name="'+o.track.name+'" value="'+o.track.id+'" type="radio" >'+o.track.name+'</li>';
                        });
                        html = html + '</ul>';
                        $('#container-canciones').empty();
                        $('#container-canciones').append(html);

                    });
            }

            $('#select-cancion').on('click',function(){
                var selectedId = $('input[name="tracks-elegibles"]:checked').val();
                var text = $('input[name="tracks-elegibles"]:checked').attr('data-name');
                $('#container-canciones-elegidas').append('<li data-id="'+selectedId +'">'+text+'</li>');
                $('#current-offset').val($('#current-offset').val() + 5);
                console.log($('#current-offset').val());
                getAndPutSongs($('#current-offset').val());
            })


            function getUserTracks(offset){
                var request = $.ajax( {
                          method: "post",
                          url: "searchSongService",
                          timeout: 200000000,
                          data: {
                            operation: "getUserTracks",
                            offset: offset
                          },
                          success: function( data ) {
                            console.log(data);
                          }
                } );
                console.log(request);
                return request;
            }

            function addSongToMyMusic(id){
                var request = $.ajax( {
                          method: "post",
                          url: "searchSongService",
                          timeout: 200000000,
                          data: {
                            operation: "addSongToMyMusic",
                            id: id
                          },
                          success: function( data ) {
                            console.log(data);
                          }
                } );
                console.log(request);
                return request;
            }

}
