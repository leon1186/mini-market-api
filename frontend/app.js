const baseUrl = "http://54.236.222.177:8000";

const TOKEN = "8af83a49c3aea0ecb8db28aa595c69cde5547308"; // your real token

const button = document.getElementById("loadBtn");
const productList = document.getElementById("productList");

button.addEventListener("click", async () => {
    try {
        const response = await fetch(`${baseUrl}/api/products/`, {
            headers: {
                "Authorization": `Token ${TOKEN}`
            }
        });

        if (!response.ok) {
            throw new Error("Failed to fetch products");
        }

        const products = await response.json();

        productList.innerHTML = "";

        products.forEach(product => {
            const div = document.createElement("div");
            div.className = "product";

            div.innerHTML = `
                <h3>${product.name}</h3>
                <p>Price: $${product.price}</p>
            `;

            productList.appendChild(div);
        });

    } catch (error) {
        console.error(error);
        productList.innerHTML = "<p>Error loading products.</p>";
    }
});










// const baseUrl = "http://54.236.222.177:8000";

// const button = document.getElementById("loadBtn");
// const productList = document.getElementById("productList");

// // Automatically use same host, but port 8000 for API
// // const baseUrl = "http://54.236.222.177:8000";

// button.addEventListener("click", async () => {
//     try {
//         const response = await fetch(`${baseUrl}/api/products/`);

//         if (!response.ok) {
//             throw new Error("Failed to fetch products");
//         }

//         const products = await response.json();

//         productList.innerHTML = "";

//         products.forEach(product => {
//             const div = document.createElement("div");
//             div.className = "product";

//             div.innerHTML = `
//                 <h3>${product.name}</h3>
//                 <p>Price: $${product.price}</p>
//             `;

//             productList.appendChild(div);
//         });

//     } catch (error) {
//         console.error(error);
//         productList.innerHTML = "<p>Error loading products.</p>";
//     }
// });
