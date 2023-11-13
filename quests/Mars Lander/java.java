import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
final class WorldSettings{
    final int maxWide = 7000; // 0 - 7000
    final int maxHigh = 3000; // 0 - 3000
    final double GRAVITY = 3.711;
    final int minPossibleAngle = -90;
    final int maxPossibleAngle = 90;
    final int minPossiblePower = 0;
    final int maxPossiblePower = 4;
    final int angleChangeLimit = 15;
    final int powerChangeLimit = 1;
    final int minLandingArea = 1000;
    final int landingAngle = 0; 
    final int landingVerticalSpeedLimit = 40;
    final int landingHorizontalSpeedLimit = 20;

}
class Surface{
    int surfacePoints;
    ArrayList<Coordinate> coordinate;
    Surface(int surfacePoints, ArrayList<Coordinate> coordinate){
        this.surfacePoints = surfacePoints;
        this.coordinate = coordinate;
    }
}
class Coordinate {
    int x;
    int y;
    Coordinate(int x, int y){
        this.x = x;
        this.y = y;
    }
}
class Numbers {
    double a;
    double b;
    Numbers(double a, double b){
        this.a = a;
        this.b = b;
    }
}
class Spaceship{
    Coordinate coordinate;
    int horizontalSpeed;
    int verticalSpeed;
    int fuel;
    int rotateAngle;
    int power;
    Spaceship(Coordinate coordinate, int horizontalSpeed, int verticalSpeed, int fuel, int rotateAngle, int power){
        this.coordinate = coordinate;
        this.horizontalSpeed = horizontalSpeed;
        this.verticalSpeed = verticalSpeed;
        this.fuel = fuel;
        this.rotateAngle = rotateAngle;
        this.power = power;
    }
}
class Player {
    public static void main(String args[]) {
        WorldSettings worldSettings = new WorldSettings();
        Surface surface;
        ArrayList<Coordinate> landingZone = new ArrayList<Coordinate>();
        Spaceship spaceship;
        String command = "0 3";
        Scanner in = new Scanner(System.in);
        int surfaceN = in.nextInt(); // the number of points used to draw the surface of Mars.
        ArrayList<Coordinate> surfaceCoordinates = new ArrayList<Coordinate>();
        for (int i = 0; i < surfaceN; i++) {
            int landX = in.nextInt(); // X coordinate of a surface point. (0 to 6999)
            int landY = in.nextInt(); // Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
            surfaceCoordinates.add(new Coordinate(landX,landY));
        }
        surface = new Surface(surfaceN,surfaceCoordinates);
        //** FIND FLAT */
        landingZone = findFlatArea(surface.coordinate);
        if(landingZone.size() == 2 ){System.err.println("Landing zone: FOUND");}
        // game loop
        while (true) {
            int X = in.nextInt();
            int Y = in.nextInt();
            int hSpeed = in.nextInt(); // the horizontal speed (in m/s), can be negative.
            int vSpeed = in.nextInt(); // the vertical speed (in m/s), can be negative.
            int fuel = in.nextInt(); // the quantity of remaining fuel in liters.
            int rotate = in.nextInt(); // the rotation angle in degrees (-90 to 90).
            int power = in.nextInt(); // the thrust power (0 to 4).
            Coordinate coordinateSpaceship = new Coordinate(X, Y);
            spaceship = new Spaceship(coordinateSpaceship, hSpeed, vSpeed, fuel, rotate, power);

            int moveingDirection = 0;
            if((spaceship.coordinate.x > landingZone.get(0).x) && (spaceship.coordinate.x < landingZone.get(1).x)){
                System.err.println("IN LANDING AREA");
                if((Math.abs(spaceship.horizontalSpeed) > worldSettings.landingHorizontalSpeedLimit)||(Math.abs(spaceship.verticalSpeed) > worldSettings.landingVerticalSpeedLimit - 10)) {
int angleRot = (int) Math.toDegrees(Math.asin((double)spaceship.horizontalSpeed/((double) Math.sqrt((spaceship.horizontalSpeed * spaceship.horizontalSpeed) + (spaceship.verticalSpeed * spaceship.verticalSpeed)))));
                    if(spaceship.coordinate.y - landingZone.get(0).y  > 30){
                        command = angleRot +" "+ worldSettings.maxPossiblePower ;
                    }else{
                        command = "0 "+ "4";
                    }
                }else{
                    command = "0 "+ "0";
                }
            }
            else{
                if(spaceship.coordinate.x >(landingZone.get(0).x + worldSettings.minLandingArea)){
                    System.err.println("LANDING AREA ON LEFT");
                    moveingDirection = 1;
                }else{
                    System.err.println("LANDING AREA ON RIGHT");
                    moveingDirection = -1;
                }    
                if( (Math.abs(spaceship.horizontalSpeed) > 4 * worldSettings.landingHorizontalSpeedLimit) || //za wolno
                    ((spaceship.coordinate.x < landingZone.get(0).x) && (spaceship.horizontalSpeed < 0))|| // w złym kierunku
                    ((spaceship.coordinate.x > landingZone.get(1).x) && (spaceship.horizontalSpeed > 0))){
                        int angleRot = (int) Math.toDegrees(Math.asin((double)spaceship.horizontalSpeed/((double) Math.sqrt((spaceship.horizontalSpeed * spaceship.horizontalSpeed) + (spaceship.verticalSpeed * spaceship.verticalSpeed)))));
                        command = angleRot +" 4";
                }else if ( (Math.abs(spaceship.horizontalSpeed) <2 * worldSettings.landingHorizontalSpeedLimit)){                          
                    int angleRot = moveingDirection * ((int) Math.toDegrees(Math.acos(worldSettings.GRAVITY / 4.0)));
                    command = angleRot + " 4";
                }else{
                    if(spaceship.verticalSpeed<5)
                    {
                        command = "0 4";
                    }else {command =  "0 3";}
                }
            }
            System.err.println("Landing zone: X: |"+landingZone.get(0).x+" : "+landingZone.get(1).x+"| Y: |" +landingZone.get(0).y+" |");
            System.out.println((command));
        }
    }
    public static ArrayList<Coordinate> findFlatArea(ArrayList<Coordinate> coordinates){
        ArrayList<Coordinate> finalCoordinates = new ArrayList<Coordinate>();
        WorldSettings worldSettings = new WorldSettings();
        for(int i=0; i<coordinates.size();i++){
            Coordinate coordinate_1 = coordinates.get(i);
            Coordinate coordinate_2;
            if((i+2)>coordinates.size()){
                System.err.println("End of Array: " +i+ " : " + coordinates.size());
                break;
            }else{
                coordinate_2 = coordinates.get(i+1);
            }
            if(coordinate_1.y == coordinate_2.y ){
                finalCoordinates.add(coordinate_1);
                finalCoordinates.add(coordinate_2);
            }        
        }
        return finalCoordinates;
    }
}
