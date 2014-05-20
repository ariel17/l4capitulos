/*
 * Common implementation for 4Capitulos project.
 */

function set_goback(id) {
    $(id).click(function(){
        parent.history.back();
        return false;
    });
}
