$(document).ready(function () {

	$('.go_to').click(function () {
		var scroll_el = $(this).attr('href');
		if ($(scroll_el).length != 0) {
			$('html, body').animate({ scrollTop: $(scroll_el).offset().top }, 900);
		}
		return false;
	});

	/*---------------------------------------------------end*/

	$(function () {
		function showModal(id) {
			$(id).fadeIn();
		}
		function hideModals() {
			$(document.body).removeClass('is-open-modal');
			$('.modal').fadeOut();
		};

		$('.order_btn').on('click', function (e) {
			event.preventDefault()
			showModal('#modal_1');
		});

		$('.modal-close').on('click', function () {
			hideModals();
		});
		$(document).on('click', function (e) {
			if (!(
				($(e.target).parents('.modal-content').length)
				|| ($(e.target).hasClass('modal-content'))
				|| ($(e.target).hasClass('btn'))
				|| ($(e.target).hasClass('order_btn'))
				|| ($(e.target).hasClass('heading'))
			)
			) {
				hideModals();
			}
		});

	});
	/*---------------------------------------------------end*/

	$(window).scroll(function () {
		if ($(window).scrollTop() > 83) {
			$('header').addClass('fixed');
		}
		else {
			$('header').removeClass('fixed');
		}
	})

	/*---------------------------------------------------end*/

	$('.menuBtn').on('click', function () {
		$(this).toggleClass("active");
		$('.header-nav').slideToggle();
	});

});

