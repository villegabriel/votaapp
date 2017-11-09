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
                          }
                } );
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
                          }
                } );
                return request;
            }
            function addTracksToPlaylist(ids, plid){
                var request = $.ajax( {
                          method: "post",
                          url: "searchSongService",
                          timeout: 200000000,
                          data: {
                            operation: "addTracksToPlaylist",
                            ids:  JSON.stringify(ids),
                            plid: plid
                          },
                          success: function( data ) {
                          }
                } );
                return request;
            }

            $('#confirm-list').on('click', function(){

            });

            $('#confirm-playlist').on('click', function(){
                var arreglo = [];
                $('#container-canciones-elegidas').find('li').each(function(){
                    arreglo.push($(this).attr('data-id'));
                });
                if($('input[name="playlist-to-add"]:checked').length){
                    var selectedPlayListId = $('input[name="playlist-to-add"]:checked').val();
                    addTracksToPlaylist(arreglo, selectedPlayListId);
                } else if($('#newListName').val() != ''){
                }

            })
}
