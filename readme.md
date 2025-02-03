# Git Submodule Management Guide for DataDog Variables

This guide will help you manage the Git submodule located at `src/datadog` in the [DataDog-Variables repository](https://github.com/DepoIQ/DataDog-Variables.git).

## Table of Contents

1. [Adding the Submodule](#adding-the-submodule)
2. [Updating the Submodule](#updating-the-submodule)
3. [Pushing Changes to the Submodule](#pushing-changes-to-the-submodule)
4. [Pulling Changes from the Submodule](#pulling-changes-from-the-submodule)

---

## Adding the Submodule

To add the DataDog Variables repository as a submodule in your own repository, follow these steps:

1. **Navigate to Your Main Repository**

   Open your terminal and navigate to the directory of the main repository where you want to add the submodule.

   ```bash
   cd /path/to/your/main/repo
   ```

2. Add the Submodule

   Use the following command to add the submodule. Replace `<submodule-path>` with the desired path where the submodule will reside (e.g., `src/datadog`):


   ```bash
   git submodule add https://github.com/DepoIQ/DataDog-Variables.git <submodule-path>
   ```
   
   Example:

   ```bash
   git submodule add https://github.com/DepoIQ/DataDog-Variables.git src/datadog
   ```

3. Initialize and Update the Submodule

   After adding the submodule, run the following command to initialize and fetch the submodule content:

   ```bash
   git submodule update --init --recursive
   ```

4. Commit the Changes

   After adding the submodule, commit this change to your main repository:

   ```bash
   git add .gitmodules <submodule-path>
   git commit -m "Added DataDog-Variables as a submodule"
   ```

   Example:

   ```bash
   git add .gitmodules src/datadog
   git commit -m "Added DataDog-Variables as a submodule"
   ```

5. Push the Changes to Remote

   Finally, push the changes to the remote repository:

   ```bash
   git push origin main
   ```

## Updating the Submodule

To update the submodule to the latest commit in its remote repository, follow these steps:

1. Navigate to the submodule directory:

   ```bash
   cd <submodule-path>
   ```

2. Pull the latest changes:

   ```bash
   git pull origin main
   ```

3. Navigate back to the main project directory:

   ```bash
   cd <main-project-path>
   ```

4. Commit the updated state of the submodule:

   ```bash
   git add <submodule-path>
   git commit -m "Updated DataDog-Variables submodule"
   git push
   ```

## Pushing Changes to the Submodule
If you make changes to the files in the submodule, you can push those changes back to the remote repository:

1. Navigate to the submodule directory:

   ```bash
   cd src/datadog
   ```

2. Stage and commit your changes:

   ```bash
   git add .
   git commit -m "Your commit message"
   ```

3. Push the changes to the remote repository:

   ```bash
   git push origin master  # or the relevant branch name
   ```

4. Navigate back to the main project directory:

   ```bash
   cd ../../
   ```

5. Commit the updated submodule reference:

   ```bash
   git add src/datadog
   git commit -m "Update submodule reference to latest commit"
   git push
   ```

## Pulling Changes from the Submodule

To pull changes made to the submodule from its remote repository:

1. Navigate to the submodule directory:

   ```bash
   cd src/datadog
   ```

2. Pull the latest changes:

   ```bash
   git pull origin master  # or the relevant branch name
   ```

3. Navigate back to your main project directory:

   ```bash
   cd ../../
   ```

4. Commit the updated submodule reference:

   ```bash
   git add src/datadog
   git commit -m "Update submodule reference after pulling changes"
   git push
   ```
