/**
 * Assignment 7
 */

/** album-info component should display songs and album cover **/
Vue.component('album-info',{
    props: ["album_id"],
    template: `
    <div id="album_info">
        <div id="album_cover">
        </div>
        <div id="album_songs">
        </div>
    </div>
    `,
})
