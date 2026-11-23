function validateForm(data) {
  const title = typeof data?.title === "string" ? data.title.trim() : "";
  const subject = typeof data?.subject === "string" ? data.subject.trim() : "";

  if (title.length < 3 || title.length > 60) {
    return "Title must be between 3 and 60 characters.";
  }

  if (!subject) {
    return "Please choose a subject.";
  }

  const resources = Array.isArray(data.resources) ? data.resources : [];
  const normalizedTitle = title.toLowerCase();
  const normalizedSubject = subject.toLowerCase();
  const duplicate = resources.some((resource) =>
    typeof resource?.title === "string" &&
    typeof resource?.subject === "string" &&
    resource.title.trim().toLowerCase() === normalizedTitle &&
    resource.subject.trim().toLowerCase() === normalizedSubject
  );

  return duplicate ? "Already on your shelf" : "";
}
