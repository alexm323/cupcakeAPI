const BASE_URL = "http://localhost:5000/api"







$("#new-cupcake-form").on('submit', async function (evt) {
    evt.preventDefault();
    let flavor = $("#flavor").val();
    let size = $("#size").val();
    let rating = $("#rating").val();
    let image = $("#image").val();

    newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        size,
        rating,
        image
    });
    // console.log(newCupcakeResponse)
    let newCupcake = $(createCupcakeHTML(newCupcakeResponse.data.cupcake))
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
})

function createCupcakeHTML(cupcake) {
    return `
    <div data-id=${cupcake.id}>
        <li>
        ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
        <button class="delete-button">X</button>
        </li>
        <img class="cupcake-image"
            src="${cupcake.image}"
            alt="(No image provided)">
    </div>
    `;
}

async function getCupcakes() {
    const response = await axios.get(`${BASE_URL}/cupcakes`);

    for (let cupcake of response.data.cupcakes) {
        let newCupcake = $(createCupcakeHTML(cupcake));
        $("#cupcakes-list").append(newCupcake);
    }
}

// $("#show-cupcakes-button").on("click", getCupcakes)
// showCupcakesButton = document.getElementById("show-cupakes-button")


$('#cupcakes-list').on('click', ".delete-button", async function (evt) {
    evt.preventDefault();

    let $cupcake = $(evt.target).closest("div");
    const cupcakeId = $cupcake.attr("data-id");
    //We need to include the route that we are going to send our delete string to. Dont forget in javascript we use back ticks to create a string template literal
    await axios.delete(`/api/cupcakes/${cupcakeId}`);
    //this is currently referencing a button so in jquery we can remove the parent
    $cupcake.remove();

})

$(getCupcakes);

