function publish(){

    var title = document.getElementById("title-input").value;
    var author = document.getElementById("author-input").value;
    var story = document.getElementById("story-input").value;

    var blog_data = {
        "title" : title,
        "author" : author,
        "story" : story
    }

    fetch(`${window.origin}/create_post/`, {

        method: "POST",
        credentials: "include",
        body: JSON.stringify(blog_data),
        cache: 'no-cache',
        headers: new Headers({
            "content-type" : "application/json"
        })

    }).then(function (response){

        response.json().then(function(data){
            console.log(data)
        })

    })

}