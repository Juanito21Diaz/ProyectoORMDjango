google.charts.load("current", {packages:["corechart"]});
// google.charts.setOnLoadCallback(drawChart);
$(function(){
    google.charts.setOnLoadCallback(graficar);

})

function drawChart() {

    $.ajax({
        url: 'grafica1GOOGLE',
        dataType: 'json',
        type: 'post',
        cache:false,
        async: false,
        succes: function(resultado){
            console.log(resultado);
            var data = google.visualization.arrayToDataTable(resultado.datos);
            var option = {
                title: 'Ventas de FUFAS',
                legend: 'none',

            }
            var grafica = document.getElementById('grafica');
            var chart = new google.visualization.ColumChark(grafica);
            
        }
    })
        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Work',     11],
          ['Eat',      2],
          ['Commute',  2],
          ['Watch TV', 2],
          ['Sleep',    7]
        ]);

        var options = {
          title: 'My Daily Activities',
          is3D: true,
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
        chart.draw(data, options);
}