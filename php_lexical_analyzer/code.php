<?php
    /* Implementing recursive binary search
    in an array using PHP */

    function RecursiveBinarySearch($array,$search,$left,$right)
    {
        if($left > $right)
        {
            return -1;
        }

        $average_element_index = floor(($left + $right)/2);
        $average_element = $array[$average_element_index]

        $comparision_result = strcmp($search,$average_element);

        if($comparision_result == 0)
        {
            return $average_element_index;
        }
        else
        {
            if($comparision_result > 0)
            {
                $left = $average_element_index + 1;
                return RecursiveBinarySearch($array,$search,$left,$right);
            }
            else
            {
                $right = $average_element_index + 1;
                return RecursiveBinarySearch($array,$search,$left,$right)
            }
        }
    }
?>