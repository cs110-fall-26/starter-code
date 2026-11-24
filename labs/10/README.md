# Lab 10: Portfolio Web App

In this lab, you will update the `server.py`, implementing the functionality for editing a project and deleting a project. The base HTML has been created for you already.

Additionally, you will also update the `index.html` to include more information. My example include programming languages and additional context for the about me portion. You must include at least 2 new sections that are relevant to yourself to gain full credit for this assignment.

## Task

1. Update the bio portion in the `index.html` to include a tag-line about yourself. This can be brief but should describe you.
2. Next, add two sections below the projects about yourself. These should be relevant to you.
3. Now, turn your attention to the `server.py` and implement the `edit_project` function.
    a. This function will find the project at the index of `project_id - 1` and update the name and description to the values passed in from the form.
    b. It should then save the projects back out.
    c. Lastly, redirect the user back to the `/projects` path.
4. After implementing `edit_project`, implement `delete_project`.
    a. This function will find the project with index of `project_id - 1` and delete that project from the list of projects.
    b. it should then save the projects back out.
    c. Lastly, redirect the user back to the `/projects` path.
4. If everything works correctly, you should be able to view projects on the home page, and in the `/projects` path. Keep in mind that the home page only shows the first 5 projects. Additionally, the new project form is in the `/projects` path. Edit and Delete exist on the inividual project, which is found when clicking on the > symbol next to the project.
5. As a final task, add more styles to the page. This time, `styles/styles.css` will read correctly within each page. A default style has been created. You may add more to it and change the format to your hearts desire.

## Quick Notes

- Some of the style classes are written in the html but aren't defined or used in the styles.css file. You may edit them and change the styles to what you'd like.

