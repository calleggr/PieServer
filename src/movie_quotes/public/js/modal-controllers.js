/* ### Modal Controllers ### */
(function() {
  var app = angular.module("modal-controllers", [ "ui.bootstrap"]);

  app.controller("InsertQuoteModalCtrl", function ($modalInstance, $timeout, movieQuoteInModal, MovieQuotes) {
    this.isNewQuote = movieQuoteInModal == undefined;
    movieQuoteInModal = movieQuoteInModal || {};
    this.quoteValue = movieQuoteInModal.quote || "";
    this.movieValue = movieQuoteInModal.movie || "";

    this.insertQuote = function () {
      movieQuoteInModal.quote = this.quoteValue;
      movieQuoteInModal.movie = this.movieValue;
      movieQuoteInModal.last_touch = new Date();
      //TODO
      if(this.isNewQuote) {
        MovieQuotes.save(movieQuoteInModal);
      } else {
        MovieQuotes.update({id: movieQuoteInModal._id}, movieQuoteInModal);
      }
      $modalInstance.close(movieQuoteInModal);
    };

    this.cancel = function () {
       $modalInstance.dismiss("cancel");
    };

    $modalInstance.opened.then(function() {
      $timeout(function() {
        // Note the opened promise is still too early.  Added a 100mS delay to give Chrome time to put the DOM in place.
        document.querySelector("#quote-input").focus();
      }, 100);
    });
  });


	app.controller("DeleteQuoteModalCtrl", function ($modalInstance, movieQuoteInModal, MovieQuotes) {
	  this.deleteQuote = function () {
	    //TODO
      MovieQuotes.delete({id: movieQuoteInModal._id}, movieQuoteInModal);
	    $modalInstance.close(movieQuoteInModal);
	  };

	  this.cancel = function () {
	     $modalInstance.dismiss("cancel");
	  };
	});

})();
