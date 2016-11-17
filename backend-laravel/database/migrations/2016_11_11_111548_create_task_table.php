<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateTaskTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('articles', function(Blueprint $table)
        {
            $table->increments('id')->unsigned();
            $table->float('input_max_emit_power')->unsigned();
            $table->float('input_max_emit_frequency');
            $table->float('input_antenna_height');
            $table->float('input_antenna_gain');
            $table->float('input_antenna_ratio');
            $table->float('input_noise_figure');
            $table->float('input_feeder_loss');
            $table->float('input_station_wide');
            $table->longText('input_direction');

            $table->float('user_max_emit_power')->unsigned();
            $table->float('user_max_emit_frequency');
            $table->float('user_antenna_height');
            $table->float('user_antenna_gain');
            $table->float('user_antenna_ratio');
            $table->float('user_noise_figure');
            $table->longText('user_direction');


            $table->float('radar_antenna_height');
            $table->float('radar_antenna_gain');
            $table->float('radar_antenna_ratio');
            $table->float('radar_noise_figure');
            $table->float('radar_antenna_tilt');
            $table->float('radar_interference_threshold');
            $table->float('radar_wide');
            $table->longText('radar_direction');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        //
    }
}
