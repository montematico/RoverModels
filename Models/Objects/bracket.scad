//A SCAD file to generate a bracket of any angle for building

/* [Beam Parameters] */
bracket_angle = 90; //[45: 180]
beam_width = 15; //brace width in mm incase larger or smaller model neccecary (X)
beam_height = 15; //brace height in mmm incase larger or smaller model neccecary (Z)

/* [Bracket Parameters] */
//thickness of bracket walls, expressed in mm
wall_thickness = 2;
//The length of the bracket in mm, set to 0 to use default ratio
bracket_length = 0;
if(bracket_length == 0)
{
    bracket_length = (beam_width + beam_height) * (1.6); // takes the average of X,Z and multiplies it by 3.2

}
/* [Other Parameters] */
//The extra margin that should be added to the bracket compared to the beam size. Interpreted as a percentage of the beamsize
margin = 0; //

/* [Hidden] */
slop = 1 + (margin/100);

//creates a simulated beam profile which can create a cut extrude
//offset = brace_width/2
module beam(beam_width = 15, beam_height = 15, bracket_angle = 90)
{
    union()
    {
        XYoffset = beam_width/-2;
        Zoffset = beam_height/-2;
        translate([XYoffset,XYoffset,Zoffset])
        {
            cube([beam_width,bracket_length,beam_height],center= false);
        }
        
        translate([0,0,0])
        {
            rotate(-bracket_angle)
            {   
                translate([XYoffset,XYoffset,Zoffset])
                {
                    cube([beam_width,bracket_length,beam_height],center= false);
                }
            }
        }
    }
}

/*
module bracket(wall_thickness, length, angle, make_printable = false)
{
    //use 2d shapes and duplicate/ extrude them
    
    if(make_printable)
    {
        //Put the little foot to add a printable surface here
    }

}
*/
module bracket_tube(beam_width = 15,beam_height = 15,wall_thickness = 3,slop = 1, length = 0)
{
    if (length == 0)
    {
        length = bracket_length;
        echo(length);
        echo(bracket_length);
    }
    beam = [beam_width * slop:beam_height*slop];

    linear_extrude(length)
    {
        difference()
         {
                square([5,5],true);
                //square(size = [beam.x + wall_thickness , beam.y + wall_thickness], true); //Forms the outer square
                //square(size = [beam.x,beam.y], true); //forms the inner square
        }
    }
}


beam();