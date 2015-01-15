'use strict';

module.exports = function(grunt) {

  // Load grunt tasks automatically
  require('load-grunt-tasks')(grunt);

  // Time how long tasks take
  require('time-grunt')(grunt);

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      dist: {
        options: {
          sourcemap: true,
          style: 'compressed'
        },
        files: {
          'elections/static/css/app.css': 'elections/static/scss/app.scss'
        }
      }
    },

    watch: {
      sass: {
        files: ['elections/static/scss/**/*.scss'],
        tasks: ['sass']
      }
    }

  });

  grunt.registerTask('default', ['sass']);
  grunt.registerTask('dev', ['default', 'watch']);
};
