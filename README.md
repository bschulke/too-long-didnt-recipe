# too-long-didnt-recipe
For everyone who hates the long stories people add to their recipe articles.

By [@bschulke](https://github.com/bschulke) and [@aibhleog](https://github.com/aibhleog)

## Previously on our show, we: 
* looking into the subsections in the HTML for some recipes
  * for the ingredients list, they're set up the same as the `<div>`s used in the ofThing part of the lists, hence why it's read into the code and throws off the order in that table
  * for the steps list, they're an `<h3>` object one layer above the rest, so the code currently reads in only the first subsection of directions.
* identified pieces of the gods awful class names that could be helpful building our ingredients list and steps
  * for the portion/amounts, there is "... Amount-Wcygw ..."
  * for the ofThing/Description, there is "... Description-dSowHq ..."
  * for the step number, there is "... InstructionHed-czmoes ..."
  * for the steps, there is "... InstructionBody-huriqk ..."

## Action items // to do:

* figure out how to replace the `find_elements_by_tag_name` sections (that pulled the `<p>` and `<div>` info to make the table) and replace with the specific class keywords:
  * check "previously on our show" to see what the class name fragments are
* **NEXT TIME**: need to account for subsections in the STEPS part and/or the INGREDIENTS
  * see if there are special tags for these subheader titles?  **answer** for the subheaders in the ingredients list, there is "... SubHed-eHJCch ..."; for the subheaders in the steps section, there is '... InstructionGroupHed-hQmgGS ...'
* test on multiple BonAppetit recipes


### Stretch goals:
* saving file info -- first time run prompt user to specify location/path if not inside repo?
* user input?
* ADD A RECIPE SCALING OPTION (like "double this recipe" or "halve this recipe")


### SUPER Stretch goals:
* make this a basic HTML website, where you input the URL of the recipe and it will output the ingredients and steps on the website.
  * consider caching recipes that have been run?
  * give option to save recipe to file
* what if we made this into a mobile app that can be used as a plugin on a web browser?
* test on other non-BonAppetit recipe websites!

### Thoughts:
For this script version, we need to think about how it will work out of the box for any user.
