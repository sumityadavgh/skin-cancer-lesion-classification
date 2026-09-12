const CLASS_NAMES = {
    "akiec": "Actinic Keratoses",
    "bcc": "Basal Cell Carcinoma",
    "bkl": "Benign Keratosis-like Lesions",
    "df": "Dermatofibroma",
    "mel": "Melanoma",
    "nv": "Melanocytic Nevi",
    "vasc": "Vascular Lesions"
};



const imageInput = document.getElementById("imageInput");
const imagePreview = document.getElementById("imagePreview");
const fileName = document.getElementById("fileName");

const predictButton = document.getElementById("predictButton");
const loading = document.getElementById("loading");

const result = document.getElementById("result");
const predictedClass = document.getElementById("predictedClass");
const confidence = document.getElementById("confidence");
const confidenceFill = document.getElementById("confidenceFill");
const resetButton = document.getElementById("resetButton");


// When user selects an image
imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    if (!file) {
        fileName.textContent = "No image selected";
        imagePreview.style.display = "none";
        return;
    }

    // Shows file name
    fileName.textContent = file.name;

    // Shows image preview
    const imageURL = URL.createObjectURL(file);

    imagePreview.src = imageURL;
    imagePreview.style.display = "block";

    // Hides previous result
    result.classList.add("hidden");

    // Shows reset button
    resetButton.classList.remove("hidden");
});


// When user clicks Predict
predictButton.addEventListener("click", async function () {

    const file = imageInput.files[0];

    // Check if image is selected
    if (!file) {
        alert("Please select an image first.");
        return;
    }

    // Create FormData
    const formData = new FormData();

    formData.append("image", file);


    // Show loading
    loading.classList.remove("hidden");

    predictButton.disabled = true;

    // Hide previous result
    result.classList.add("hidden");


    try {

        // Send image to Django API
        const response = await fetch(
            "http://127.0.0.1:8000/api/predict/",
            {
                method: "POST",
                body: formData
            }
        );


        // Convert response to JSON
        const data = await response.json();


        // Check for errors
        if (!response.ok) {
            throw new Error(data.error || "Prediction failed.");
        }


        // Display prediction
        predictedClass.textContent =
                CLASS_NAMES[data.predicted_class] || data.predicted_class;

        confidence.textContent = data.confidence;

        confidenceFill.style.width = `${data.confidence}%`;

        // Show result
        result.classList.remove("hidden");

    } catch (error) {

        alert("Error: " + error.message);

    } finally {

        // Hide loading
        loading.classList.add("hidden");

        // Enable button
        predictButton.disabled = false;
    }
});

// Reset everything
resetButton.addEventListener("click", function () {

    imageInput.value = "";

    imagePreview.src = "";
    imagePreview.style.display = "none";

    fileName.textContent = "No image selected";

    predictedClass.textContent = "";
    confidence.textContent = "";

    confidenceFill.style.width = "0%";

    result.classList.add("hidden");

    resetButton.classList.add("hidden");
});