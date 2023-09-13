const pokedex = document.getElementById("pokedex");

const fetchPokemon = async () => {
    const url = `https://pokeapi.co/api/v2/pokemon?limit=150`;
    const res = await fetch(url);
    const data = await res.json();
    const pokemon = data.results.map((result, index) => ({
        ...result,
        id: index + 1,
        image: `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${index + 1}.png`,
        apiURL: result.url,
    }))
    displayPokemon(pokemon);
}


const displayPokemon = (pokemon) => {
    const pokemonHTMLString = pokemon.map( (pokeman) => `
    <li class="card" onclick="selectPokemon(${pokeman.id})")>
        <img class="card-image" src="${pokeman.image}"/>
        <h2 class="card-title">${pokeman.id}. ${pokeman.name}</h2>
    </li>
    `).join('');
    pokedex.innerHTML = pokemonHTMLString;
}

// Function to fetch and display selected pokemon
const selectPokemon = async (id) => {
    const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
    const res = await fetch(url);
    const pokeman = await res.json();
    displayPopUp(pokeman, id);
}

const displayPopUp = (pokeman, id) => {
    console.log(pokeman);
    const pokemanId = pokeman["id"];
    const url = `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemanId}.png`
    const type = pokeman.types.map( (type) => type.type.name).join(', ');
    const stats = pokeman.stats.map( (stat) => stat.base_stat);
    console.log("this is the stats");
    console.log(stats);
    const htmlString = `
    <div class="container">
        <button id="closeBtn" onclick="fetchPokemon()">Close</button>
        <div class="popUp" onclick="selectPokemon(${pokeman.id})">
            <img class="card-image" src="${url}"/>
            <h2 class="card-title">${pokeman.id}. ${pokeman.name}</h2>
            <h3 class="card-subtitle">(${type})</h3>
            <h3 class="card-subtitle">Attack: ${stats[1]} | Defense: ${stats[2]}</h3>
            <h3 class="card-subtitle">Special-Attack: ${stats[3]} | Special-Defense: ${stats[4]}</h3>
            <h3 class="card-subtitle">Speed: ${stats[5]}</h3>
        </div>
    </div>
    `;
    pokedex.innerHTML = htmlString;
}

fetchPokemon();