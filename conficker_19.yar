import "hash"

rule Conficker_19_Infection
{
	strings: 
		$string_1 = "send_flag"
		$string_2 = "/home/jeff/Desktop/ctf_pcap_forensic_analysis/chal2"
		$encryption_routine = {8b 85 9c fd ff ff 83 c0 01 31 ca 48 98 88 94 05 d0 fe ff ff 83 85 9c fd ff ff 01 83 bd 9c fd ff ff 0e 7e b9 48 8d 95 c0 fd ff ff 48 8d 8d e0 fe ff ff 48 8d 85 d0 fe ff ff 48 89 ce 48 89 c7 e8 37 fc ff ff}
	condition: 
		$string_1 or
		$string_2 or
		$encryption_routine or
		hash.md5 (0, filesize) == "3164c55b20427dbd7ab07b9bca8ed090" or
		hash.sha256 (0, filesize) == "436a7970bd8cb1866466ce0f7b6ebc5a1cc37e32672f16db89bc91f9cea643c5"
}


