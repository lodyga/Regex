# Matching Specific String
Regex_Pattern = r'hackerrank'

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))


Input (stdin)
The hackerrank team is on a mission to flatten the world by restructuring the DNA of every company on the planet. We rank programmers based on their coding skills, helping companies source great programmers and reduce the time to hire. As a result, we are revolutionizing the way companies discover and evaluate talented engineers. The hackerrank platform is the destination for the best engineers to hone their skills and companies to find top engineers.



# Matching Anything But a Newline
regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())

Input (stdin)
123.456.abc.def


# Matching Digits & Non-Digit Characters
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
06-11-2015



# Matching Whitespace & Non-Whitespace Character

Regex_Pattern = r"\S\S\s\S\S\s\S\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
12 11 15



# Matching Word & Non-Word Character

Regex_Pattern = r"\w{3}\W\w{10}\W\w{3}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
www.hackerrank.com



# Matching Start & End
Regex_Pattern = r"^\d\w{4}.$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
0qwer.



# Matching Specific Characters
Regex_Pattern = r'^[123][120][sx0][30Aa][xsu][,\.]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
1203x.



# Excluding Specific Characters
Regex_Pattern = r'^\D[^aeiou][^bcDF]\S[^AEIUO][^,.]$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
think?



# Matching Character Ranges
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
h4CkR



# Matching {x} Repetitions
Regex_Pattern = r"^[A-Za-z02468]{40}[13579\s]{5}$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
2222222222aaaaaaaaaa2222222222aaaaaaaaaa13 57



# Matching {x, y} Repetitions
Regex_Pattern = r'^\d{1,2}[a-zA-Z]{3,}\.{,3}$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
3threeormorealphabets.



# Matching Zero Or More Repetitions
Regex_Pattern = r'^\d{2,}[a-z]*[A-Z]*$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
14



# Matching One Or More Repetitions
Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
1Qa



# Matching Ending Items
Regex_Pattern = r'^[A-z]*s$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
Kites



# Matching Word Boundaries
Regex_Pattern = r'\b[aAeEUuIiOo][A-z]*\b'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
Found any match?



# Capturing & Non-Capturing Groups
Regex_Pattern = r'.*(ok){3,}.*'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())



# Alternative Matching
Regex_Pattern = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
Mr.DOSHI



# Matching Same Text Again & Again
Regex_Pattern = r'([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([A-Za-z])([aeuioAEUIO])(\S)\1\2\3\4\5\6\7\8\9\10'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Input (stdin)
ab #1?AZa$ab #1?AZa$

Regex_Pattern = r'([a-z]\w\s\W\d\D[A-Z][A-Za-z][aeuioAEUIO]\S)\1'
Regex_Pattern = r'([a-z]\w\s\W\d\D[A-Z][A-Za-z][aeuioAEUIO]\S){2}'



# Backreferences To Failed Groups
Regex_Pattern = r"^(\d{8}|\d{2}-\d{2}-\d{2}-\d{2})$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

Valid inp
12345678
12-34-56-87

Invalid inp
1-234-56-78
12-45-7810

Regex_Pattern = r"^\d{2}(-?)(\d{2}\1){2}\d{2}$"



# Branch Reset Groups
<?php

$Regex_Pattern = '/^\d\d(-|:|---|.)(\d\d\1){2}\d\d$/'; //Do not delete '/'. Replace __________ with your regex.

$handle = fopen ("php://stdin","r");
$Test_String = fgets($handle);
if(preg_match($Regex_Pattern, $Test_String, $output_array)){
    print ("true");
} else {
    print ("false");
}

fclose($handle);
?>


Valid inp
12345678
12-34-56-87

Invalid inp
1-234-56-78
12-45-7810



# Forward References
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {    

    public static void main(String[] args) {
        
        Regex_Test tester = new Regex_Test();
        tester.checker("^(tac(tactic|tac)+)$"); // Use \\ instead of using \ 
    
    }
}

class Regex_Test {

    public void checker(String Regex_Pattern){
    
        Scanner Input = new Scanner(System.in);
        String Test_String = Input.nextLine();
        Pattern p = Pattern.compile(Regex_Pattern);
        Matcher m = p.matcher(Test_String);
        System.out.println(m.find());
    }   
    
}

^((tac)+(tactic|tac)+)+$

Valid
tactactic
tactactactactic
tactactictactic
Invalid
tactactictactictictac
tactictac



# Positive Lookahead
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {    

    public static void main(String[] args) {
        
        Regex_Test tester = new Regex_Test();
        tester.checker("o(?=oo)"); //Use '\\' instead of '\'.
    
    }
}

class Regex_Test {

    public void checker(String Regex_Pattern){
    
        Scanner Input = new Scanner(System.in);
        String Test_String = Input.nextLine();
        Pattern p = Pattern.compile(Regex_Pattern);
        Matcher m = p.matcher(Test_String);
        int Count = 0;
        while(m.find()){
            Count += 1;
        }
        System.out.format("Number of matches : %d",Count);
    }   
    
}

Input (stdin)
gooooo!



# Negative Lookahead
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {    

    public static void main(String[] args) {
        
        Regex_Test tester = new Regex_Test();
        tester.checker("(.)(?!\\1)"); //Use '\\' instead of '\'.
    
    }
}

class Regex_Test {

    public void checker(String Regex_Pattern){
    
        Scanner Input = new Scanner(System.in);
        String Test_String = Input.nextLine();
        Pattern p = Pattern.compile(Regex_Pattern);
        Matcher m = p.matcher(Test_String);
        int Count = 0;
        while(m.find()){
            Count += 1;
        }
        System.out.format("Number of matches : %d",Count);
    }   
    
}

Input (stdin)
gooooo



# Positive Lookbehind
Regex_Pattern = r"(?<=[13579])\d"	# Do not delete 'r'.

import re

Test_String = raw_input()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)

Input (stdin)
123Go!



# Negative Lookbehind
Regex_Pattern = r"(?<![aeuioAEUIO])."	# Do not delete 'r'.

import re

Test_String = raw_input()

match = re.findall(Regex_Pattern, Test_String)

print "Number of matches :", len(match)


Input (stdin)
1o1s

(?i)(?<![aeiou]).

# Detect HTML Tags





