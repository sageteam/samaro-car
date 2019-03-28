# CSS Class naming instruction

Here you can learn about css learning into SCSS files.

## File seperation

Basic sub-foldering of SCSS:

* dashboard
  * home.scss
  * settings.scss
  * profile.scss

* pages
  * langing.scss
  * registration.scss
  * faq.scss

* partials
  * navigation
  * footer
  * header

* permanent
  * fonts
  * mixin
  * colors
  * buttons

## File Naming

CSS classed must not be dependent together. Because we need to develop modules of css files. For example one time we design a form class in bootstrap 3 with responsive capability. Another time if you want to use the same design in another website, you will use your previous scss files and import them into your new project.

Here we show some examples:

* .form
  * .form .txtbox
    * .form .txtbox .icon
  * .form .choicefield
    * .form .choicefield .icon
  * .form .button

* .banner
  * .banner .text
  * .banner .table
    * .banner .table .tbl-row

* backgrounds
  * .form-bg
  * .banner-bg

* NOTES:
  * use em and rem for font sizes.
  * read end of font.scss
  * read end of colors.scss