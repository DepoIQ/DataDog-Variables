# Git Submodule Management Guide for DataDog Variables

This guide will help you manage the Git submodule located at `src/datadog` in the [DataDog-Variables repository](https://github.com/DepoIQ/DataDog-Variables.git).

## Table of Contents

1. [Adding the Submodule](#adding-the-submodule)
2. [Adding the Submodule with Branch Tracking](#adding-the-submodule-with-branch-tracking)
3. [Updating the Submodule](#updating-the-submodule)
4. [Pushing Changes to the Submodule](#pushing-changes-to-the-submodule)
5. [Pulling Changes from the Submodule](#pulling-changes-from-the-submodule)

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

## Adding the Submodule with Branch Tracking

To add the DataDog Variables repository as a submodule that tracks a specific branch (instead of a specific commit), follow these steps:

1. **Navigate to Your Main Repository**

   Open your terminal and navigate to the directory of the main repository where you want to add the submodule.

   ```bash
   cd /path/to/your/main/repo
   ```

2. **Add the Submodule**

   Use the following command to add the submodule. Replace `<submodule-path>` with the desired path and `<branch-name>` with the branch you want to track:

   ```bash
   git submodule add -b <branch-name> https://github.com/DepoIQ/DataDog-Variables.git <submodule-path>
   ```
   
   Example (tracking the `development` branch):

   ```bash
   git submodule add -b development https://github.com/DepoIQ/DataDog-Variables.git src/datadog
   ```

3. **Configure Branch Tracking**

   Configure the submodule to track the specified branch:

   ```bash
   git config -f .gitmodules submodule.<submodule-path>.branch <branch-name>
   ```

   Example:

   ```bash
   git config -f .gitmodules submodule.src/datadog.branch development
   ```

4. **Initialize and Update the Submodule**

   Initialize and fetch the submodule content:

   ```bash
   git submodule update --init --recursive --remote
   ```

5. **Commit the Changes**

   Commit the submodule configuration to your main repository:

   ```bash
   git add .gitmodules <submodule-path>
   git commit -m "Added DataDog-Variables as a submodule tracking <branch-name> branch"
   ```

   Example:

   ```bash
   git add .gitmodules src/datadog
   git commit -m "Added DataDog-Variables as a submodule tracking development branch"
   ```

6. **Push the Changes to Remote**

   Finally, push the changes to the remote repository:

   ```bash
   git push origin main
   ```

**Note:** When a submodule tracks a branch, you can update it to the latest commit of that branch using `git submodule update --remote` instead of manually navigating to the submodule directory.

## Updating the Submodule

### For Commit-Based Submodules

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

### For Branch-Tracking Submodules

To update a branch-tracking submodule to the latest commit of the tracked branch:

1. **From the main repository directory, run:**

   ```bash
   git submodule update --remote <submodule-path>
   ```

   Example:

   ```bash
   git submodule update --remote src/datadog
   ```

2. **Commit the updated submodule reference:**

   ```bash
   git add <submodule-path>
   git commit -m "Updated DataDog-Variables submodule to latest commit on tracked branch"
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
