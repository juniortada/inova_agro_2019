// Author: Junior Tada

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
		submit: function(event){
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
    				$('#form_producao').submit();
    			}
			}
			catch(err){
    			console.log(err);
    		}
		},
	},
});