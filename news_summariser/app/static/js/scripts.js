document.getElementById("fetchForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const url = document.getElementById("url").value;
    const outputDiv = document.getElementById("output");

    outputDiv.innerHTML = `
        <div class="text-center">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p>Processing...</p>
        </div>
    `;

    fetch("/fetch", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url })
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.articles) {
                outputDiv.innerHTML = `<h3>Fetched ${data.articles.length} Articles:</h3>`;
                data.articles.forEach((article, index) => {
                    outputDiv.innerHTML += `
                        <div class="article-card">
                            <a href="${article.url}" target="_blank"><h4>${index + 1}. ${article.title || "No Title"}</h4></a>
                            <p><b>Extractive Summary</b> <br />${article.summary_extractive || "Not available"}</p>
                            <p><b>Abstractive Summary</b> <br />${article.summary_abstractive || "Not available"}</p>
                            <p><b>Sentiment</b> <br />${article.sentiment || "Not available"}</p>
                            <p><b>Date Published</b> <br />${article.published || "Unknown Date"}</p>
                        </div>
                    `;
                });
            } else {
                outputDiv.innerHTML = `
                    <a href="${data.url}" target="_blank"><h4>${data.title || "No Title"}</h4></a>
                    <p><b>Extractive Summary</b> <br/> ${data.summary_extractive || "Not available"}</p>
                    <p><b>Abstractive Summary</b> <br />${data.summary_abstractive || "Not available"}</p>
                    <p><b>Sentiment</b> <br />${data.sentiment || "Not available"}</p>
                    <p><b>Date Published</b> <br />${data.published || "Unknown Date"}</p>
                `;
            }
        })
        .catch(() => {
            outputDiv.innerHTML = "<p class='text-danger'>Error fetching the data. Please try again.</p>";
        });
});
