/* [Beam Parameters] */

/* [Bracket Parameters] */

/* [Other Parameters] */








inner_square = 15;
outer_sqaure = 18;
length = 48;
angle = 90;

difference()
{
    union()
    {
        translate([0, 0, outer_sqaure/-2]) {
            linear_extrude(length)
            {
                difference()
                {
                    square(outer_sqaure,true);
                    square(inner_square,true);
                }
            }
        }
        translate([outer_sqaure/-2,0,0])
        {
            rotate([0,angle,0])
            {
                linear_extrude(length)
                {
                    difference()
                    {
                        square(outer_sqaure,true);
                        square(inner_square,true);
                    }
                }
            }
        }
    }

    translate([inner_square/-2,inner_square/-2,inner_square/2])
    {
        rotate([0,0,0])
        {
            union()
            {
                cube([inner_square,inner_square,length],false);
                rotate([0,angle,0])
                {
                    cube([inner_square,inner_square,length],false);
                }
            }
        }
    }
}
