var lc = document.getElementById("location").value;	
	$(document).ready(function(){
		$("#"+lc).removeClass();
		$("#"+lc).addClass("current");	
		$("#shouye").hover(
		  function () {
			$(this).addClass("current");
		  },
		  function () {
		    if(lc!="shouye"){
				$(this).removeClass("current");
			}
		  });	
		$("#qylc").hover(
		  function () {
			$(this).addClass("current");
			$("#qylc_sub").show();
		  },
		  function () {
		    if(lc!="qylc"){
				$(this).removeClass("current");
			}
			$("#qylc_sub").hide();
		  });			
		$("#zlwh").hover(
		  function () {
			$(this).addClass("current");
			$("#zlwh_sub").show();
		  },
		  function () {
		    if(lc!="zlwh"){
				$(this).removeClass("current");
			}
			$("#zlwh_sub").hide();
		  });			
		$("#xwzx").hover(
		  function () {
			$(this).addClass("current");
			$("#xwzx_sub").show();
		  },
		  function () {
		    if(lc!="xwzx"){
				$(this).removeClass("current");
			}
			$("#xwzx_sub").hide();
		  });			
		$("#tdfc").hover(
		  function () {
			$(this).addClass("current");
			$("#tdfc_sub").show();
		  },
		  function () {
		    if(lc!="tdfc"){
				$(this).removeClass("current");
			}
			$("#tdfc_sub").hide();
		  });			
		$("#fwwd").hover(
		  function () {
			$(this).addClass("current");
		  },
		  function () {
		    if(lc!="fwwd"){
				$(this).removeClass("current");
			}
		  });			
		$("#jrwm").hover(
		  function () {
			$(this).addClass("current");
			$("#jrwm_sub").show();
		  },
		  function () {
		    if(lc!="jrwm"){
				$(this).removeClass("current");
			}
			$("#jrwm_sub").hide();
		  });
	$("#qylc_sub").hover(
	  function () {
		$("#qylc").addClass("current");
		$(this).show();
	  },
	  function () {
		  if(lc!="qylc"){
		$("#qylc").removeClass("current");
		  }
		$(this).hide();
	  });	  
	$("#zlwh_sub").hover(
	  function () {
		$("#zlwh").addClass("current");
		$(this).show();
	  },
	  function () {
		  if(lc!="zlwh"){
		$("#zlwh").removeClass("current");
		  }
		$(this).hide();
	  });	  
	$("#xwzx_sub").hover(
	  function () {
		$("#xwzx").addClass("current");
		$(this).show();
	  },
	  function () {
		  if(lc!="xwzx"){
		$("#xwzx").removeClass("current");
		  }
		$(this).hide();
	  });	  
	$("#tdfc_sub").hover(
	  function () {
		$("#tdfc").addClass("current");
		$(this).show();
	  },
	  function () {
		  if(lc!="tdfc"){
		$("#tdfc").removeClass("current");
		  }
		$(this).hide();
	  });	  
	$("#jrwm_sub").hover(
	  function () {
		$("#jrwm").addClass("current");
		$(this).show();
	  },
	  function () {
		  if(lc!="jrwm"){
		$("#jrwm").removeClass("current");
		  }
		$(this).hide();
	  });	
	});