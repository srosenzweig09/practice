public class GuessGame {
    Player Suzanne;
    Player CJ;
    Player p3;
    Player Jasmin;

    public void startGame() {
        Suzanne = new Player();
        CJ = new Player();
        p3 = new Player();
        Jasmin = new Player();

        int guessSuzanne = 0;
        int guessCJ = 0;
        int guessp3 = 0;
        int guessJasmin = 0;

        boolean SuzanneisRight = false;
        boolean CJisRight = false;
        boolean p3isRight = false;
        boolean JasminisRight = false;

        int targetNumber = (int) (Math.random() * 10);
        System.out.println("I'm thinking of a number between 0 and 9...");

        while(true) {

            // guess is a method of the Player class
            // we know this because Suzanne is an instance of the Player class
            // and the .guess() after Suzanne says we are accessing the guess method of the Player class for Player Suzanne
            Suzanne.guess();

            CJ.guess();

            p3.guess();
            p3.cheat();

            Jasmin.guess();

            guessSuzanne = Suzanne.number;
            System.out.println("Player one guessed " + guessSuzanne);
            
            guessCJ = CJ.number;
            System.out.println("Player two guessed " + guessCJ);
            
            guessp3 = p3.number;
            System.out.println("Player three guessed " + guessp3);
            
            // guessJasmin is a variable because it's followed by an = sign
            guessJasmin = Jasmin.number;
            System.out.println("Player four guessed " + guessJasmin);

            if (guessSuzanne == targetNumber) {
                SuzanneisRight = true;
            }
            if (guessCJ == targetNumber) {
                CJisRight = true;
            }
            if (guessp3 == targetNumber) {
                p3isRight = true;
            }
            if (guessJasmin == targetNumber) {
                JasminisRight = true;
            }

            if (SuzanneisRight || CJisRight || p3isRight || JasminisRight) {
                System.out.println("We have a winner!");
                System.out.println("Player one got it right? " + SuzanneisRight);
                System.out.println("Player two got it right? " + CJisRight);
                System.out.println("Player three got it right? " + p3isRight);
                System.out.println("Jasmin got it right? " + JasminisRight);
                System.out.println("Game is over.");
                break;
            } else {
                System.out.println("Players will have to try again.");
                System.out.println();
            }
        }
    }
}
