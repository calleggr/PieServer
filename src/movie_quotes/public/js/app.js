(function() {
  var app = angular.module("app", [ "ui.bootstrap", "modal-controllers", "ngResource" ]);

  app.controller("MovieQuotesCtrl", function($scope, $modal, MovieQuotes) {
    this.items = [];
    this.navbarCollapsed = true;
    this.isEditing = false;

    this.showInsertQuoteDialog = function(movieQuoteFromRow) {
      this.navbarCollapsed = true;
      var modalInstance = $modal.open({
        templateUrl : "/partials/insertQuoteModal.html",
        controller : "InsertQuoteModalCtrl",
        controllerAs : "insertModal",
        resolve : {
          movieQuoteInModal : function() {
            return movieQuoteFromRow;
          }
        }
      });
      var movieQuotesCtrl = this;
      modalInstance.result.then(function(movieQuoteFromModal) {
        if (movieQuoteFromRow != null) {
          var index = movieQuotesCtrl.items.indexOf(movieQuoteFromModal);
          if (index > -1) {
            movieQuotesCtrl.items.splice(index, 1);
          }
        }
        movieQuotesCtrl.items.unshift(movieQuoteFromModal);
        movieQuotesCtrl.isEditing = false;
      });
    };

    this.showDeleteQuoteDialog = function(movieQuoteFromRow) {
      var modalInstance = $modal.open({
        templateUrl : "/partials/deleteQuoteModal.html",
        controller : "DeleteQuoteModalCtrl",
        controllerAs : "deleteModal",
        resolve : {
          movieQuoteInModal : function() {
            return movieQuoteFromRow;
          }
        }
      });
      var movieQuotesCtrl = this;
      modalInstance.result.then(function(movieQuoteFromModal) {
        var index = movieQuotesCtrl.items.indexOf(movieQuoteFromModal);
        if (index > -1) {
          movieQuotesCtrl.items.splice(index, 1);
        }
        movieQuotesCtrl.isEditing = false;
      });
    };

    this.listMovieQuotes = function() {
      //TODO
      this.items = MovieQuotes.query();
    };

    // Make the initial backend request.
    this.listMovieQuotes();

    // Check to see if more quotes need to be loaded.
    var movieQuotesCtrl = this;
    window.addEventListener("scroll", function(ev) {
      if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        movieQuotesCtrl.listMovieQuotes();
      }
    });

  });

  app.factory('MovieQuotes', ['$resource', function($resource){
    return $resource('/api/moviequotes/:id', null, {
      'update': { method:'PUT' }
    });
  }])
})();
