public class GameLauncher {

    public static void main (String[] args) {

        System.out.println();

        GuessGame game = new GuessGame();
        
        // game is a GuessGame object
        game.startGame();

        System.out.println();
    }
}