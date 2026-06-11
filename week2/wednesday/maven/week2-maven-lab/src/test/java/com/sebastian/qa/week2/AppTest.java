package com.sebastian.qa.week2;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

public class AppTest {

    @Test
    public void shouldAnswerWithTrue() {
        assertTrue(true);
    }

    @Test
    public void greeterReturnsGreetingForName() {
        Greeter greeter = new Greeter();

        assertEquals("Hello, Sebastian", greeter.hello("Sebastian"));
    }

    @Test
    public void greeterThrowsExceptionForBlankName() {
        Greeter greeter = new Greeter();

        assertThrows(IllegalArgumentException.class, () -> greeter.hello(""));
    }

}
