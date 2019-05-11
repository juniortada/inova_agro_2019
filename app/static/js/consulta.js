// Author: Junior Tada

// grafico

google.charts.load('current', {'packages':['bar']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
	var data = google.visualization.arrayToDataTable([
	  ['Valor', 'Valor Verificado', 'Máximo', 'Mínimo'],
	  ['CCS', 200000, 500000, 200000],
	  ['CMT', 250000, 500000, 200000],
	  ['CBT', 100000, 300000, 200000]
	]);


	var options = {
	  chart: {
	    title: 'Qualidade das Amostras',
	    subtitle: 'CCS, CMT, CBT',
	  },
	  bars: 'horizontal' // Required for Material Bar Charts.
	};

	var chart = new google.charts.Bar(document.getElementById('barchart_1'));

	chart.draw(data, google.charts.Bar.convertOptions(options));


	var data2 = google.visualization.arrayToDataTable([
	  ['Valor', 'Valor Verificado', 'Máximo', 'Mínimo'],
	  ['Gordura', 20, 50, 3.0],
	  ['Proteína', 2.5, 5.0, 2.9],
	  ['Lactose', 5, 6, 4.3],
	  ['Sólidos', 10, 30, 11.4]
	]);


	var options2 = {
	  chart: {
	    title: 'Qualidade das Amostras',
	    subtitle: 'Gordura, Proteína, Lactose, Sólidos',
	  },
	  bars: 'horizontal' // Required for Material Bar Charts.
	};

	var chart2 = new google.charts.Bar(document.getElementById('barchart_2'));

	chart2.draw(data2, google.charts.Bar.convertOptions(options2));
}


// inicializa vue
var app = new Vue({
	el: '#app1',

	data:{
		produtores: [],
		produtor: ''
	},

	// método que executa inicialização da pagina
	mounted: function(){
		this.$nextTick(function (){
			this.buscarProdutores();
		})
	},

	methods: {
		// busca todos os produtores e adiciona no select option
    	buscarProdutores: function(event){
    		var self = this;
	        $.ajax({
	            url: '/agro/_produtores',
	            method: 'GET',
	            success: function(data){
	                self.produtores = data.produtores;
	            },
	            error: function(error){
	                console.log(error);
	            }
	        });
		},
		// submit
		validar: function(event){
			try{
				var self = this;
    			// valida produtor
    			if(self.produtor === '' || self.produtor === null){
    				$('#titulo_erro').text('Escolha um Produtor');
	    			$('#msg_erro').text('Nenhum produtor selecionado, por favor escolha um produtor!');
	    			$('#modal_erro').modal('show');
    			}
    			else{
    				$('#produtor_id').val(self.produtor);
    				/*$('#form_producao').submit();*/
    			}
			}
			catch(err){
    			console.log(err);
    		}
		},
	},
});

