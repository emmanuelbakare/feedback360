;(function(){
    // var id
    // var modal=new bootstrap.Modal(document.getElementById("modelId"))
    // console.log('Welcome to Django')
    // document.querySelectorAll('.item-list').forEach(item=>{
    //     item.addEventListener('dblclick', (e)=>{
    //         // alert('You Clicked '+e.target.id)
    //         id=e.target.id
    //         console.log('you clicked '+id)
    //     })
    // })

    // window.onclick = e => {
    //     tag=htmx.closest(e.target, 'li')
    //     removeactive(tag) // remove highlight from any li that is already highlighted
    //     htmx.addClass(tag,'activeli') // highlight the clicked li
    // } 



    window.addEventListener('DOMContentLoaded',function(e){
        elems=document.querySelectorAll('body')
        elems.forEach(item=>{
            // item.classList.remove('activeli')
            item.addEventListener('click',function(evt){
                if(evt.target.nodeName=="LI" ){
                        clearUnclicked(evt.target,'activeli')
                }
                if(evt.target.className=="obj-item"){
                    parent=evt.target.parentNode 
                    clearUnclicked(parent,'activeli')
                }
            })

            // item.addEventListener('mouseover',function(evt){
            //     if(evt.target.nodeName=="LI" ){
            //             clearUnclicked(evt.target,'hoverli')
            //     }
            //     if(evt.target.className=="obj-item"){
            //         parent=evt.target.parentNode 
            //         clearUnclicked(parent,'hoverli')
            //     }
            // })

            // item.addEventListener('mouseout',function(evt){
            //     if(evt.target.nodeName=="LI" ){
            //             clearUnclicked(evt.target,'outli')
            //     }
            //     if(evt.target.className=="obj-item"){
            //         parent=evt.target.parentNode 
            //         clearUnclicked(parent,'outli')
            //     }
            // })
    
        })
    })




    
})()

function clearUnclicked(clickedli,classname){
    ul =clickedli.parentNode 
    lis=ul.getElementsByTagName('li')
    Array.from(lis).forEach(li=>{
         li.classList.remove(classname)
    })
    clickedli.classList.add(classname)

}

function removeactive(elem){
    ul=htmx.closest(elem,'ul') // get the closest ul to the clicked element
    lis=ul.querySelectorAll('li') // get all the li under that ul
    
    lis.forEach(e=>{ //loop through each li and remove the active class
        htmx.removeClass(e,'activeli')
    })
}