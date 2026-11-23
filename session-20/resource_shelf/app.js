const storageKey = "resourceShelfData";
const form = document.getElementById("resourceForm");
const titleInput = document.getElementById("title");
const subjectInput = document.getElementById("subject");
const formError = document.getElementById("formError");
const resourceList = document.getElementById("resourceList");

function loadResources() {
  const savedData = localStorage.getItem(storageKey);

  if (savedData === null) {
    return [];
  }

  try {
    const parsedData = JSON.parse(savedData);
    if (!Array.isArray(parsedData)) {
      return [];
    }

    return parsedData.filter((resource) =>
      resource &&
      typeof resource.title === "string" &&
      typeof resource.subject === "string"
    );
  } catch (error) {
    if (error instanceof SyntaxError) {
      formError.textContent = "Saved data was damaged; starting fresh";
      return [];
    }
    throw error;
  }
}

let resources = loadResources();

function renderResources() {
  resourceList.replaceChildren();

  for (const resource of resources) {
    const item = document.createElement("li");
    const title = document.createElement("span");
    const subject = document.createElement("span");
    title.textContent = resource.title;
    subject.textContent = resource.subject;
    subject.className = "subject";
    item.append(title, subject);
    resourceList.append(item);
  }
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const data = {
    title: titleInput.value,
    subject: subjectInput.value,
    resources
  };
  const error = validateForm(data);

  if (error) {
    formError.textContent = error;
    return;
  }

  const updatedResources = [
    ...resources,
    { title: data.title.trim(), subject: data.subject.trim() }
  ];

  try {
    localStorage.setItem(storageKey, JSON.stringify(updatedResources));
  } catch (error) {
    formError.textContent = "Could not save your resource. Please try again.";
    return;
  }

  resources = updatedResources;
  formError.textContent = "";
  form.reset();
  renderResources();
});

renderResources();
